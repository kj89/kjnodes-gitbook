# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.8.4-mainnet | **Wasm**: ON

[Website](https://kujira.app) | [Discord](https://discord.gg/teamkujira) | [Twitter](https://twitter.com/TeamKujira)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/kujira](https://explorer.kjnodes.com/kujira)

## Public endpoints

* api: [https://kujira.api.kjnodes.com](https://kujira.api.kjnodes.com)
* rpc: [https://kujira.rpc.kjnodes.com](https://kujira.rpc.kjnodes.com)
* grpc: kujira.grpc.kjnodes.com:13090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@kujira.rpc.kjnodes.com:13656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@kujira.rpc.kjnodes.com:13659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/kujira/addrbook.json > $HOME/.kujira/config/addrbook.json
```

**live-peers** (29)
```bash
peers="1fb8ef552bf812a15d0d81ffbc8a3eb77b4319e6@65.21.231.176:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,89757803f40da51678451735445ad40d5b15e059@169.155.45.187:26656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,bd2821b2dc8b928946026caf3e9bd1e7a0013a61@145.239.10.46:13656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,3a15fa46fe0a27d4ee60497a470a8c91911a9e5e@15.235.66.89:11756,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,413bd0410b649de5070b2fe8356cad356459dc37@65.108.235.165:26656,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656,0c7da38c54e1a7d8ab7d48601b51847564ce019e@5.161.91.34:45656,0cd7caa189ab5e3fb19b4d32516027b578ab7838@45.79.118.43:26656,c8b74590ce04f0f7c32b1c668290e00ec7ec275e@148.113.8.63:11856,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,42e9c232f830e39824747ce6a4e5ef1e765cad72@67.222.144.195:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,897c55fb33076c9cecc56f6c04e2a3cbed195e7c@185.248.24.20:26796,de08e6178779ff3b19a8b6d22a05664392cb2b35@185.216.179.205:26656,ab587b4bf216c348657ed3dde85d1f48c5ad279c@15.235.115.155:10004,af9465035c6111c6cedddd7bdee60c78a8f9921c@54.235.174.123:26656,459229e89fd0722f7f758b7de782d0eb94aa9639@146.59.85.223:11856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
