; ModuleID = "main"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

@"true" = constant i1 1
@"false" = constant i1 0
define i32 @"add"(i32 %".1", i32 %".2")
{
add_entry:
  %".4" = alloca i32
  store i32 %".1", i32* %".4"
  %".6" = alloca i32
  store i32 %".2", i32* %".6"
  %".8" = load i32, i32* %".4"
  %".9" = load i32, i32* %".6"
  %".10" = add i32 %".8", %".9"
  ret i32 %".10"
}

define i32 @"main"()
{
main_entry:
  %".2" = call i32 @"add"(i32 2, i32 3)
  %".3" = alloca [10 x i8]*
  store [10 x i8]* @"__str_1", [10 x i8]** %".3"
  %".5" = bitcast [10 x i8]* @"__str_1" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", i32 %".2")
  %".7" = call i32 @"add"(i32 1, i32 2)
  ret i32 %".7"
}

@"__str_1" = internal constant [10 x i8] c"apples %i\00"