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

**live-peers** (29)
```bash
peers="da843d721574dd06d04b6fa32c9d7d552a376bf4@178.128.238.183:26120,a0a450ead908bd65813322c1373802ef32c5736d@65.108.235.33:4000,d851052ed8a1c66dc90208b992f393602c26d786@57.128.82.243:33656,59c74642d0ec4d012dd7bd0a7e5af1eadf2061b2@65.109.30.183:26656,4236750928a4dcb742e50e30e500ebc9ee39f240@35.223.246.103:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:49656,e39876398a43c0f9b93b5a82d8e38fa57c0373b5@65.109.89.19:20756,dfb44159d26b62affd7112367e082b2397bbff15@65.108.136.206:26656,dfe5f91f824880e19d47475546d9874e0f2cea8c@5.79.74.229:8095,51ca404bbc73d07fc0d6529388c90f807c5acf0b@65.109.104.72:20756,8a9e42026a687b2762cefbd74584ccbd6afa0be1@65.109.83.124:26656,175ca82ab5b282549d68d79ff2c3703d26bcacef@141.94.109.71:20757,777f8dee1a8278fd5d9319dab55625dcc4ae1677@162.19.57.180:24356,347e6fa3c974e91aee92da5793486ba3f1bae67d@23.88.112.67:26656,98e489fc375c4dd26eb0d2410fab4e1ab049f61b@144.126.141.236:26656,80be85c4980deccaa2fbd710029f0eb660dadf9a@51.81.16.186:26656,f7dede5bd05eb9615c8c6fa273e25bd4f10f56b8@65.108.109.240:3000,9cb7ba30c7eb7e9b516b90e09ca0f53250927440@146.59.52.135:8095,aedf3405d57c3efdcc2bdb1d571dc10f05247f08@51.89.40.85:22656,744f2ecd98984eb0e20640ca4b7be69c0be0b81d@45.83.106.141:26656,e91f650bb3d5b66762093150718af358c6355cc5@15.235.10.35:36656,462a37ca052c4d058e505959393574045dce9489@116.202.36.240:20756,3b3428d679faa1bd498b3554ca798de3a0d802c6@162.19.89.8:20756,56a59158450e6f819502812cf28febd65c1ac6be@206.189.26.213:26120,a46ad42b84690a2af0071f20337182b3bfba75fc@38.146.3.130:20756,70d1818f50d983bfebf4c8546b221687b76cd4b0@51.81.107.95:20756,9f55d181ba68c2a7b62d065fa5974bc1ada7395f@188.165.252.51:26656,cf75b4e7c27d950181964e99bab6c7aaf330a312@85.214.64.99:26956,6870906f86e474d88d077c7c55af36debe49da04@178.162.165.194:7095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.migalood/config/config.toml
```
