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

**live-peers** (30)
```bash
peers="b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,f46cdadb43b2078fba2a8b261e0109c18967fdaf@95.214.55.140:21156,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,c8b74590ce04f0f7c32b1c668290e00ec7ec275e@148.113.8.63:11856,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,55d5419822feeab727b2be57e834534cbd91d6a4@65.108.69.91:26656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,1cbc1bff7cdaeffd5a25583f9525f44fb55f7215@95.214.54.28:26156,7554d02b3ea3049267e5a8bb2851f85035998f96@172.177.106.103:26656,fb5b72024981de8ea392876c8409fe60a439d699@54.235.174.123:26656,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,0a03f5dfb5b995647808c4d100e7b98d0526302f@85.214.18.167:26656,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.5.20:26656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,dfbe5a5892a2da543e0324cfb6ee87fbf6f6f60e@212.23.222.98:21156,0cd7caa189ab5e3fb19b4d32516027b578ab7838@45.79.118.43:26656,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,3a15fa46fe0a27d4ee60497a470a8c91911a9e5e@15.235.66.89:11756,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,fa925ef53799d2cf30b317ac52759871909b151c@44.206.174.98:26656,44cdb43183527cad8a3a9b032532e1b4422e53e7@24.158.14.210:26656,4d3ecadfa5002bdd407c56c04933999b8f96cfbd@34.173.154.254:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
