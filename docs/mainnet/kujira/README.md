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
peers="c1a740841a6dc0b56730e975b1a4aa2d8c73b204@65.108.237.233:29656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,0cd7caa189ab5e3fb19b4d32516027b578ab7838@45.79.118.43:26656,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,1d436f8d9a36e7d93d897012dd4e98871e8c4fbb@65.108.137.37:26656,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,09076c7908db88316498cf4cd4702a8d269e0da9@15.235.114.85:26656,4c22af952c3af002136397d48f9933d0432ace7a@148.251.79.204:26656,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.5.20:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,75cd9d2f96a352eb429e166e69b45cb1dfb99d06@65.108.200.49:9556,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,fdde823fb8c9ef908d4b229f177c5f8b18e90274@54.235.174.123:26656,beb3329e969ae64d97c276f0ed0a1773ebdf61dc@146.19.24.142:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,a430d40d7c4272a649b8309abed412f562057539@3.37.223.124:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26796"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
