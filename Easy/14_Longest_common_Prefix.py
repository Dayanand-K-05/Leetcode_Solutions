# https://leetcode.com/problems/longest-common-prefix/description/
def longestCommonPrefix(strs):
  if not strs:
    return ""
  for i in range(len(strs[0])):
    char = strs[0][i]
    for other in strs[1:]:
      if i >= len(other) or other[i] != char:
        return strs[0][:i]
  return strs[0]

result = longestCommonPrefix(["flower", "flow", "flight"])
print(result)
