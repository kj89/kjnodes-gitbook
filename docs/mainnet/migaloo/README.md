# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/migaloo.png" width="150" alt=""><figcaption></figcaption></figure>

The Migaloo chain is a permissionless Cosmos SDK chain on which  projects are encouraged to build their applications. Migaloo chain  is the home of the White Whale dApp, Interchain Command Center.

**Chain ID**: migaloo-1 | **Latest Version Tag**: v2.0.2 | **Wasm**: ON

[Website](https://whitewhale.money) | [Discord](https://discord.gg/AyvcgD4jy3) | [Twitter](https://twitter.com/WhiteWhaleDefi)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/migaloo/migaloovaloper1jxtgnfw3tatfh90ju9j76dfrt3yea0zw2vnr8v)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/migaloo/migaloovaloper1jxtgnfw3tatfh90ju9j76dfrt3yea0zw2vnr8v) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/migaloo](https://explorer.kjnodes.com/migaloo)

## Public endpoints

* api: [https://migaloo.api.kjnodes.com](https://migaloo.api.kjnodes.com)
* rpc: [https://migaloo.rpc.kjnodes.com](https://migaloo.rpc.kjnodes.com)
* grpc: migaloo.grpc.kjnodes.com:49090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@migaloo.rpc.kjnodes.com:49656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@migaloo.rpc.kjnodes.com:49659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/migaloo/addrbook.json > $HOME/.migalood/config/addrbook.json
```

**live-peers** (30)
```bash
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:49656,0326c9ee117587b7ebe3b26b00820642a8cf48ff@65.108.238.102:20756,2e756df28be5e4fa7d332ba732a160202ef86eee@167.235.21.165:26656,32eed8c4079201b143d92860c9146b1d9e126aa2@168.119.89.8:26656,462a37ca052c4d058e505959393574045dce9489@116.202.36.240:20756,2051b0770ad5f02f939bd4b057b8e26f1e87e7b0@84.244.95.249:26656,78f0f5aa89b7ed92a5728dd3f67f646d8dda5213@198.244.228.162:55736,e91f650bb3d5b66762093150718af358c6355cc5@15.235.10.35:36656,9f55d181ba68c2a7b62d065fa5974bc1ada7395f@188.165.252.51:26656,70d1818f50d983bfebf4c8546b221687b76cd4b0@51.81.107.95:20756,dfb44159d26b62affd7112367e082b2397bbff15@65.108.136.206:26656,8a9e42026a687b2762cefbd74584ccbd6afa0be1@65.109.83.124:26656,9780ea85f4d0f4cb5ebca14992ce11ebe1982d35@188.172.229.26:26656,59c74642d0ec4d012dd7bd0a7e5af1eadf2061b2@65.109.30.183:26656,a0a450ead908bd65813322c1373802ef32c5736d@65.108.235.33:4000,da843d721574dd06d04b6fa32c9d7d552a376bf4@178.128.238.183:26120,fe04ff9a13d8f0b23463e832f75eb5c845bd375e@213.239.214.73:7095,d20e91b12956469860da37a8e538305dad8d23d4@185.119.118.110:4000,9cb7ba30c7eb7e9b516b90e09ca0f53250927440@146.59.52.135:8095,0c38efdc028867765e68f02979958468384ad087@51.89.155.2:23656,e39876398a43c0f9b93b5a82d8e38fa57c0373b5@65.109.89.19:20756,2fd235d3f0a1a84abd197dcfdaf04fdabc092db8@168.119.62.80:26656,51ca404bbc73d07fc0d6529388c90f807c5acf0b@65.109.104.72:20756,3b3428d679faa1bd498b3554ca798de3a0d802c6@162.19.89.8:20756,5429bc670b77cd9c61481912ea194bea8aa6d0cd@51.81.155.189:20756,6c42aacf3939d503bad695d86108d214680e04a8@144.76.175.189:20756,8ab347211b90560a0dca64ef0e4eef29012f2f67@65.109.71.119:26656,5f51850777594edef5a6077d99f794c3bf9b17fb@85.214.138.54:26656,c616069071f0864b5b0e995f8d8961536b41ab62@15.204.141.36:26656,aedf3405d57c3efdcc2bdb1d571dc10f05247f08@51.89.40.85:22656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.migalood/config/config.toml
```
