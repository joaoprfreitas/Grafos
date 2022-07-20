#include <iostream>
#include <list>
#include <vector>
#include <iomanip>
#include <fstream>
#include <queue>
#include <cmath>

using namespace std;

class Vert{
public:
    Vert() {
        adj = new list<pair<unsigned,unsigned>>;
        raiz = false;
    };
    ~Vert() {
        delete adj;
    };    
    void printAresta() {
        for (list<pair<unsigned,unsigned>>::iterator it = this->adj->begin(); it != this->adj->end(); it++) {
            cout << "VertId: " << it->first << "- W: " << it->second << endl;
        }
        cout << endl;
    }
    unsigned VertId;
    bool raiz;
    Vert* pai;
    list<pair<unsigned,unsigned>>* adj;
};

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
            a->VertId = i;          
            Verts.push_back(a);            
        }        
    }    
    void arco (unsigned v1, unsigned v2, unsigned weight) {
        this->Verts[v1-1]->adj->push_back(pair<unsigned,unsigned>(v2-1,weight));
    }
    void aresta(unsigned v1, unsigned v2, unsigned weight) {
        this->Verts[v1-1]->adj->push_back(pair<unsigned,unsigned>(v2-1,weight));
        this->Verts[v2-1]->adj->push_back(pair<unsigned,unsigned>(v1-1,weight));
    }
    void readPajek(string fileName){
        string vertices, tipo;
        unsigned size, v1, v2, weight;

        fstream fs(fileName, fstream::in);
        fs >> vertices >> size;
        this->insert(size);

        fs >> tipo;

        if (tipo == "*Arcs") {            
            while(!fs.eof()) {
                fs >> v1 >> v2 >> weight;
                this->arco(v1,v2,weight);
            }
        } else {
            while(!fs.eof()) {
                fs >> v1 >> v2 >> weight;
                this->aresta(v1,v2,weight);
            }
        }

        fs.close();
    }
    void printGraph() {
        for (vector<Vert*>::iterator it = Verts.begin(); it != Verts.end(); it++) {
            cout << "Vertice: " << (*it)->VertId << endl;
            (*it)->printAresta();
        }
    }
    vector<Vert*> Verts;
    unsigned size;    
};

class Compare
{
public:
    bool operator() (pair<unsigned,unsigned> x , pair<unsigned,unsigned> y)
    {
        return x.second > y.second;
    }
};

unsigned * dijkstra (Graph * g, Vert * s) {
    unsigned *dist;
    bool visited[g->size];
    dist = new unsigned[g->size];    
    priority_queue<pair<unsigned,unsigned>, vector<pair<unsigned,unsigned>>, Compare> fila;

    for (size_t i = 0; i < (size_t)g->size; i++) {        
        dist[i] = 0xFFFFFFFF;                       // MAX_VALUE for unsigned, the program should 
        visited[i] = false;
    }

    dist[s->VertId] = 0;
    fila.push(pair<unsigned,unsigned>(s->VertId,dist[s->VertId]));

    while(!fila.empty()) {
        Vert *u = g->Verts[fila.top().first];
        visited[fila.top().first] = true;
        fila.pop();

        for (list<pair<unsigned,unsigned>>::iterator it = u->adj->begin(); it != u->adj->end(); it++) {
            if(visited[it->first])  continue;
            unsigned newDist = dist[u->VertId] + it->second;

            if(dist[it->first] > newDist) {
                dist[it->first] = newDist;
                fila.push(pair<unsigned,unsigned>(it->first,dist[it->first]));
            }
        }    
    }

    return dist;
}

unsigned ** dijkstraAllVerts(Graph * g) {    
    unsigned ** m;
    m = new unsigned*[g->size];
    int i = 0;
    for (vector<Vert*>::iterator it = g->Verts.begin(); it != g->Verts.end(); it++){
        m[i] = dijkstra(g,*it);
        i++;
    }
    return m;
}

int main () {
    Graph * g;
    g = new Graph;
    string pajek;
    unsigned **matriz,*w;

    cin >> pajek;
    g->readPajek(pajek);

    w = new unsigned[g->size];
    unsigned **distancia;

    distancia = new unsigned*[g->size];
    for (unsigned i = 0; i < g->size; i++){
        distancia[i] = new unsigned[g->size];     
        w[i] = 0;
    }

    matriz = dijkstraAllVerts(g);

    for (size_t i = 0; i < (size_t)g->size; i++)
        for (size_t j = 0; j < (size_t)g->size; j++) {
            unsigned newW = (unsigned)floor(log10(matriz[j][i]))+1;
            if(newW > w[i])
                w[i] = newW;
        }
    
    for (size_t i = 0; i < (size_t)g->size; i++){
        for (size_t j = 0; j < (size_t)g->size; j++)
            cout << setw(w[j]) << matriz[i][j] << " ";
        cout << endl;
    }


    for (unsigned i = 0; i < g->size; i++){
        delete[] distancia[i];
        delete[] matriz[i];
    }
    delete[] matriz;
    delete[] distancia;
    delete[] w;
    delete g;
    return 0;
}