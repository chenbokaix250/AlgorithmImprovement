#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Solution {
public:
	static bool compare(string s1, string s2){
		return s1+s2 <s2+s1; //自定义排序规则 
	}
    string minNumber(vector<int>& nums) {
        vector<string> temp;
        for(int n : nums){
            temp.push_back(to_string(n)); //整型转字符串 
        }
        sort(temp.begin(), temp.end(), compare); //按自定义规则排序 
        string ans = "";
        for(string s : temp) ans += s; //拼接 
        return ans;
    }
};