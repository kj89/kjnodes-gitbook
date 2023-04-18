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
peers="ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,861f4624276d80aa538ad446ce608910ca24940d@148.251.177.45:11656,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.5.20:26656,a7400009548180ad2b229b2acfb27b8359984346@90.68.89.146:26656,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,e557abe0e49127c3e738eca6fc816c7cf0106dec@54.235.174.123:26656,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,89757803f40da51678451735445ad40d5b15e059@169.155.45.187:26656,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,42e9c232f830e39824747ce6a4e5ef1e765cad72@67.222.144.195:26656,897c55fb33076c9cecc56f6c04e2a3cbed195e7c@185.248.24.20:26796,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,09076c7908db88316498cf4cd4702a8d269e0da9@15.235.114.85:26656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,b0e6d463380fcf9bf935c10c8b6ebe371bd34009@40.122.243.249:26656,a76e18bffe05fb1332dcd4340fc6e2b482ed38fb@195.3.222.246:26656,4af5ea231c2fe1ca8174fb627e65bc09564f313b@45.143.196.110:11856,6f3129d01218b939511cccf7e0318bfe872d97c4@65.109.33.181:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
