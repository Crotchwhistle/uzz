; ModuleID = "main"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

@"true" = constant i1 1
@"false" = constant i1 0
define i32 @"test"()
{
test_entry:
  ret i32 69
}

define i32 @"main"()
{
main_entry:
  %".2" = call i32 @"test"()
  ret i32 %".2"
}
