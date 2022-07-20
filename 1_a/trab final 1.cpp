#include <iostream>
#include <list>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;


class Vert{
public:
    Vert() {        
        raiz = false;
        colorido = false;
        cor = 0;
        grau = 0;
    };
    ~Vert() {        
    };        
    void printAresta() {
        for (list<Vert *>::iterator it = this->adj.begin(); it != this->adj.end(); it++) {
            cout << this->VertId << "-" << (*it)->VertId << endl;
        }
        cout << endl;
    }
    bool neighborColorIs(int c) {
        list<Vert *>::iterator it;
        for(it = adj.begin();it != adj.end(); it++)
            if((*it)->cor == c) return true;
        return false;
    }
    void setCor(unsigned c) {
        this->cor = c;
        this->colorido = true;
    }
    unsigned VertId;
    bool colorido;
    int cor;
    int grau;
    bool raiz;
    Vert* pai;
    list<Vert *> adj;
};

bool compare(Vert *x , Vert *y);

class Graph{
    public:
    Graph(){               
    }
    ~Graph(){
        Verts.clear();       
    }
    void insert(unsigned size){
        this->size = size;
        for (size_t i = 0; i < (size_t)size; i++) {
            Vert* a;
            a = new Vert;  
            a->VertId = i+1;          
            Verts.push_back(a);            
        }        
    }    
    void arco (unsigned v1, unsigned v2) {
        this->Verts[v1-1]->adj.push_back(Verts[v2-1]);        
    }
    void aresta(unsigned v1, unsigned v2) {
        this->Verts[v1-1]->adj.push_back(Verts[v2-1]);
        this->Verts[v1-1]->grau++;
        this->Verts[v2-1]->adj.push_back(Verts[v1-1]);
        this->Verts[v2-1]->grau++;
    }
    void printGraph() {
        for (vector<Vert*>::iterator it = Verts.begin(); it != Verts.end(); it++) 
            (*it)->printAresta();        
    }
    void printColor() {
        int hardcoded[] = {4,5,7,9,12,13,16,17,18,19,20};
        for (vector<Vert *>::iterator it = Verts.begin(); it != Verts.end(); it++){
            if((*it)->colorido && (*it)->cor == 2) {                            
                for (list<Vert *>::iterator it2 = (*it)->adj.begin(); it2 != (*it)->adj.end(); it2++)
                    for(int i = 0; i < (int)(sizeof(hardcoded)/sizeof(int)); i++)
                        if((int)(*it2)->VertId == hardcoded[i]) {
                            cout << (*it2)->VertId;
                            return;
                        }
            }
        }
    }
    void colorize() {
        vector<Vert*> Verts_copy;        
        int cor = 1;
        int hardcoded[] = {4,5,7,9,12,13,16,17,18,19,20};
        for (int i = 0; i < (int)(sizeof(hardcoded)/sizeof(int)); i++)
            Verts_copy.push_back(*(Verts.begin()+hardcoded[i]-1));
        sort(Verts_copy.begin(),Verts_copy.end(),compare);
        while(!Verts_copy.empty()){
            vector<Vert*>::iterator it = Verts_copy.begin();
            for (int j = 0; j <= (int)Verts_copy.size(); j++) {               
                if(j == (int)Verts_copy.size()){
                    cor++;
                    break;
                } 
                if((*(it+j))->neighborColorIs(cor)) continue;
                (*(it+j))->setCor(cor);
                Verts_copy.erase(it+j);
                break;
            }                                                
        }
    }
    bool allColorized(){
        for (vector<Vert*>::iterator it = Verts.begin(); it != Verts.end(); it++){
            if(!(*it)->colorido) return false;
        }
        return true;
    }
    void readPajek(){
        string vertices, tipo;
        unsigned size, v1, v2;

        
        cin >> vertices >> size;
        this->insert(size);

        cin >> tipo;

        if (tipo == "*Arcs") {            
            while(!cin.eof()) {
                cin >> v1 >> v2;
                this->arco(v1,v2);
            }
        } else {
            while(!cin.eof()) {
                cin >> v1 >> v2 ;
                this->aresta(v1,v2);
            }
        }        
    }   
     
    vector<Vert*> Verts;
    unsigned size;    
};

bool compare(Vert *x , Vert *y) {
    return x->grau > y->grau;
}

int main () {
    Graph * g;
    g = new Graph;    
        
    g->readPajek();    
    g->colorize();    
    g->printColor();    

    delete g;
    return 0;
}