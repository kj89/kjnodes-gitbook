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
peers="79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,89757803f40da51678451735445ad40d5b15e059@169.155.45.187:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,f46cdadb43b2078fba2a8b261e0109c18967fdaf@95.214.55.140:21156,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@95.217.70.62:26656,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,ed71d6328a0228cd2eac7d71451509813c660b5d@116.202.164.206:26656,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,1d436f8d9a36e7d93d897012dd4e98871e8c4fbb@65.108.137.37:26656,42e9c232f830e39824747ce6a4e5ef1e765cad72@67.222.144.195:26656,09076c7908db88316498cf4cd4702a8d269e0da9@15.235.114.85:26656,fb5b72024981de8ea392876c8409fe60a439d699@54.235.174.123:26656,b8e8c1738a49cd6143cf83287a5087c2618ebca0@141.95.47.82:30256,6cceba286b498d4a1931f85e35ea0fa433373057@88.198.128.174:26656,afc247bceddc0eeeb6cf62db6fb4f985b03dd3b0@95.214.53.191:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,4af5ea231c2fe1ca8174fb627e65bc09564f313b@45.143.196.110:11856,db40fad24d78787b3096d69081049eb88b4c1dad@31.156.88.34:26656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,c55d35ef908b74c2ddec2f47dbdb4032d7dfbcd4@23.88.69.22:27266,ef5f630a1f3fd5a8623791a91ea3cd54b1a56685@44.206.174.98:26656,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.5.20:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,0cd7caa189ab5e3fb19b4d32516027b578ab7838@45.79.118.43:26656,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
