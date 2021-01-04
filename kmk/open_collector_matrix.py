
import digitalio

from kmk.matrix import DiodeOrientation, MatrixScanner

# Keep outputs other than current from interfering when there aren't diodes in the matrix.
class OpenCollectorMatrixScanner(MatrixScanner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for pin in self.inputs:
            # Pull UP inputs.
            pin.switch_to_input(pull=digitalio.Pull.UP)

    def scan_for_changes(self):
        ba_idx = 0
        any_changed = False

        for oidx, opin in enumerate(self.outputs):
            # Current row/column to ground.
            opin.switch_to_output(value=False)

            for iidx, ipin in enumerate(self.inputs):
                # Pressed if low.
                new_val = int(not ipin.value)
                old_val = self.state[ba_idx]

                if old_val != new_val:
                    if self.translate_coords:
                        new_oidx = oidx + self.len_cols * (
                            iidx // self.rollover_cols_every_rows
                        )
                        new_iidx = iidx - self.rollover_cols_every_rows * (
                            iidx // self.rollover_cols_every_rows
                        )

                        self.report[0] = new_iidx
                        self.report[1] = new_oidx
                    else:
                        self.report[0] = oidx
                        self.report[1] = iidx

                    self.report[2] = new_val
                    self.state[ba_idx] = new_val

                    any_changed = True
                    break

                ba_idx += 1

            # No longer current row/column to hi-Z.
            opin.switch_to_input(pull=digitalio.Pull.UP)
            if any_changed:
                break

        if any_changed:
            return self.report
