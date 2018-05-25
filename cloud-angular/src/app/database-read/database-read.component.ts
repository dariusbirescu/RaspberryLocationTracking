import { Component, OnInit } from '@angular/core';
import { RestService } from '../REST-service/rest.service';

@Component({
  selector: 'app-database-read',
  templateUrl: './database-read.component.html',
  styleUrls: ['./database-read.component.css']
})
export class DatabaseReadComponent implements OnInit {

  constructor(private restService: RestService) { }

  ngOnInit(): void {
    this.getMessages();
  }

  messages: any
  getMessages(){
    this.restService.getMessages().subscribe(messages =>{
      console.log(messages);
      this.messages=messages;
    })
  }

}
