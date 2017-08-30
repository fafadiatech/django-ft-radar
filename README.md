# Django FT Radar

This is a re-usable Job Aggregator written in Django

## Authors

- Sidharth Shah {sidharth@fafadiatech.com}

## Key Featurs

1. Summary Dashboard
1. Ability to convert Lead to Opportunity
1. Listing of Leads
1. Saving Lead for Later
1. Search functionality with Facets
1. Hierarchia Category Based Organization
1. Tags
1. Ability to White List and Black List Leads
1. Internal Communication on Lead

## Key Entities

1. Category: Is a high level area by which we want to organize Leads. 
1. Source: Self explainatory, which channel that lead came from
1. Tag: Free form tag that we can associate with a lead
1. LeadStatus: Generally this is `Open, Closed, Pending`. But keeping it configurable
1. Lead: Details of a lead
1. Industry: Sector with which that Lead is associated
1. Company: Company associated with that Lead
1. CompanyContact: A Contact associated with a Lead's Company

## Usage

## Worklog

- Aug 30 2017
	- First commit