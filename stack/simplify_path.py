# https://leetcode.com/problems/simplify-path/description/

class SimplifyPath:

	def sim_path(self, path):
		stack = []
		path_var = path.split("/")
		for var in path_var:
			if var != '':
				if var == ".":
					continue
				elif var == "..":
					if len(stack) > 0:
						stack.pop()
				else:
					stack.append(var)
		return "/" + "/".join(stack)



print SimplifyPath().sim_path("/a/./b/../../c/")
print SimplifyPath().sim_path("/home/")
print SimplifyPath().sim_path("/home//foo/")
print SimplifyPath().sim_path("/../")
