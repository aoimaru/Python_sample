@echo off

echo ".cmd Executed"

for %%f in (%*) do (
  echo %%f
)

echo "Completed"