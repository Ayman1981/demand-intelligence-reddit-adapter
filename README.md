# Demand Intelligence – Reddit Adapter

**Status: Prototype — awaiting Reddit Data API approval**

This repository contains the planned read-only Reddit Data API adapter for
**Demand Intelligence**, an evidence-led B2B market research system.

Demand Intelligence helps founders, product teams, agencies and businesses
identify recurring customer problems, jobs-to-be-done, unmet needs,
objections and validation signals from permitted public conversations.

## Purpose

The Reddit adapter will retrieve permitted public Reddit posts and comments
for aggregated market research.

A typical research workflow is:

Research topic / market
→ relevant Reddit communities and discussions
→ controlled sampling
→ post/comment deduplication
→ evidence classification
→ canonical evidence ledger
→ deterministic opportunity scoring
→ aggregated market research report
→ recommended behavioral validation tests

## Intended Reddit API Usage

The integration is read-only.

It may access permitted public metadata such as:

- public post text and titles
- public comments
- Reddit post/comment IDs
- subreddit/community name
- permalinks
- publication timestamps
- public engagement metrics such as score/comment count

Reddit post and comment IDs are preserved so research evidence remains
traceable to its original source.

## What the application will NOT do

The application will not:

- create Reddit posts or comments
- send private messages
- interact with Reddit users
- access private or restricted content
- profile individual Redditors
- infer sensitive personal attributes
- use Reddit data for advertising targeting
- resell raw Reddit datasets
- present Reddit comments as representative survey data
- use Reddit content to train foundation or generative AI models

AI services may be used only to classify and summarize permitted content
within the approved market-research workflow.

## Evidence Methodology

The system distinguishes:

- observed evidence from analytical inference
- individual comments from recurring patterns
- commercial/purchase signals from proof of willingness-to-pay

A single Reddit comment or URL is not treated as independent market
corroboration.

Duplicate posts/comments are removed before analysis.

## Commercial Status

This is currently an early research prototype.

If Demand Intelligence later becomes a commercial product, Reddit data will
only be used commercially if Reddit expressly permits that use and any
required commercial agreement is in place.

## Data Architecture

Reddit Data API
→ Raw Source Records
→ Deterministic Deduplication
→ Controlled Evidence Batches
→ Evidence Classification
→ Canonical Evidence Ledger
→ Deterministic Opportunity Scoring
→ Aggregated Research Report

## Security

API credentials and secrets are never stored in this public repository.

Environment variables will be used for credentials after Reddit API access
is approved.
