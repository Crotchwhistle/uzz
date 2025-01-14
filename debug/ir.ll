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
  %".4" = alloca i32
  store i32 0, i32* %".4"
  br label %"for_loop_entry_1"
for_loop_entry_1:
  %".7" = load i32, i32* %".4"
  %".8" = icmp eq i32 %".7", 5
  br i1 %".8", label %"for_loop_entry_1.if", label %"for_loop_entry_1.endif"
for_loop_otherwise_1:
  %".24" = load i32, i32* %".2"
  ret i32 %".24"
for_loop_entry_1.if:
  br label %"for_loop_otherwise_1"
for_loop_entry_1.endif:
  %".11" = load i32, i32* %".4"
  %".12" = alloca [9 x i8]*
  store [9 x i8]* @"__str_2", [9 x i8]** %".12"
  %".14" = bitcast [9 x i8]* @"__str_2" to i8*
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", i32 %".11")
  %".16" = load i32, i32* %".4"
  store i32 %".16", i32* %".2"
  %".18" = load i32, i32* %".4"
  %".19" = add i32 %".18", 1
  store i32 %".19", i32* %".4"
  %".21" = load i32, i32* %".4"
  %".22" = icmp slt i32 %".21", 10
  br i1 %".22", label %"for_loop_entry_1", label %"for_loop_otherwise_1"
}

@"__str_2" = internal constant [9 x i8] c"i = %i\0a\00\00"