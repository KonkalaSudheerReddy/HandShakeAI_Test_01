# Introduced bug verification proof

This folder records the deliberate negative test used to prove that the verifier
rejects an incorrect solution.

The temporary bug changed `total_requests` from the correct value of `6` to
`999`. The verifier then reported one failed test and wrote a reward of `0`.

The submitted `solution/solve.sh` was restored after this proof was collected.
The bugged script in this folder is evidence only and is not the active solution.

Files:

- `solve.sh.bugged`: the deliberately incorrect solution script.
- `Bug_results.txt`: the readable verifier output and result.
- `reward.txt`: the generated scalar reward.
- `ctrf.json`: the generated CTRF test report.
