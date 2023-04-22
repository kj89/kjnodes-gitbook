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
peers="c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,d21056f3e4fd703ca99f75de46a6cc5983339585@65.108.137.37:26656,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095,1fb8ef552bf812a15d0d81ffbc8a3eb77b4319e6@65.21.231.176:26656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,fa925ef53799d2cf30b317ac52759871909b151c@44.206.174.98:26656,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,9c8826ceeb1254d16856092a50df4fd720910362@50.116.49.237:26656,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,58fc044463399f5c2d94a39e3474ea6196dab0bd@65.108.198.118:11856,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,55d5419822feeab727b2be57e834534cbd91d6a4@65.108.69.91:26656,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,af9465035c6111c6cedddd7bdee60c78a8f9921c@54.235.174.123:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,698529d303400cc4dff026c6c47eb0dc6547b595@95.216.43.190:36346,b580a8e8f0936eddbafc54f0bd7ad50452022a34@70.37.167.18:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,1cbc1bff7cdaeffd5a25583f9525f44fb55f7215@95.214.54.28:26156,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,35af92154fdb2ac19f3f010c26cca9e5c175d054@65.108.238.61:27656,935c1065ad23338a5e6a75f08fb650f9f46dbd3e@65.108.201.167:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.5.20:26656,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
