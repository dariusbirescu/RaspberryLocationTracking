import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DatabaseReadComponent } from './database-read.component';

describe('DatabaseReadComponent', () => {
  let component: DatabaseReadComponent;
  let fixture: ComponentFixture<DatabaseReadComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DatabaseReadComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DatabaseReadComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();  
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
