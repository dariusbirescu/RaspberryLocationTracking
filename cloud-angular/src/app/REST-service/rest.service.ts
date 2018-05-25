import { Injectable } from "@angular/core";
import { Headers, Http } from "@angular/http";
import "rxjs/add/operator/map";
import "rxjs/add/operator/toPromise";

@Injectable()
export class RestService {
  constructor(private http: Http) {}

  private myURL = "https://locationtrackingdd.firebaseio.com/destinations.json";
  private BogdanURL= "https://locationtrackingdd.firebaseio.com/"

  getMessages() {
    return this.http.get(this.myURL).map(res=> res._body);
  }

  getUsers(){
    return this.http.get(this.BogdanURL).map(res => res.json());
  }

  postMessage(body){
    return this.http.post(this.myURL+"api/",body).map(res => res.json());
  }

  postUser(body){
    return this.http.post(this.BogdanURL,body).map(res => res.json());
  }
}