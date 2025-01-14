; ModuleID = "main"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

@"true" = constant i1 1
@"false" = constant i1 0
define i32 @"main"()
{
main_entry:
  %".2" = alloca i32
  store i32 0, i32* %".2"
  %".4" = load i32, i32* %".2"
  %".5" = icmp slt i32 %".4", 10
  br i1 %".5", label %"while_loop_entry_1", label %"while_loop_otherwise_1"
while_loop_entry_1:
  %".7" = load i32, i32* %".2"
  %".8" = alloca [9 x i8]*
  store [9 x i8]* @"__str_2", [9 x i8]** %".8"
  %".10" = bitcast [9 x i8]* @"__str_2" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i32 %".7")
  %".12" = load i32, i32* %".2"
  %".13" = add i32 %".12", 1
  store i32 %".13", i32* %".2"
  %".15" = load i32, i32* %".2"
  %".16" = icmp slt i32 %".15", 10
  br i1 %".16", label %"while_loop_entry_1", label %"while_loop_otherwise_1"
while_loop_otherwise_1:
  %".18" = load i32, i32* %".2"
  ret i32 %".18"
}

@"__str_2" = internal constant [9 x i8] c"a = %i\0a\00\00"