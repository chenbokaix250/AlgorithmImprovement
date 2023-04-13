
int x = 26 ;
string out;
stringstream ss;
ss << std::hex <<x;
ss >> out ;
transform(out.begin(), out.end(), out.begin(), ::toupper);
cout << out <<endl;
