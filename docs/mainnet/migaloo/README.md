# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/migaloo.png" alt=""><figcaption></figcaption></figure>

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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:49656,2fd235d3f0a1a84abd197dcfdaf04fdabc092db8@168.119.62.80:26656,80be85c4980deccaa2fbd710029f0eb660dadf9a@51.81.16.186:26656,8a9e42026a687b2762cefbd74584ccbd6afa0be1@142.132.207.247:36656,da843d721574dd06d04b6fa32c9d7d552a376bf4@178.128.238.183:26120,9f0da7688c30a76bd2870288f861018179e421a0@65.108.130.171:26656,3b3428d679faa1bd498b3554ca798de3a0d802c6@162.19.89.8:20756,175ca82ab5b282549d68d79ff2c3703d26bcacef@141.94.109.71:20757,e39876398a43c0f9b93b5a82d8e38fa57c0373b5@65.109.89.19:20756,fe04ff9a13d8f0b23463e832f75eb5c845bd375e@213.239.214.73:7095,d20e91b12956469860da37a8e538305dad8d23d4@185.119.118.110:4000,ea8ec0c9613b8c096938469c499a6b1e3372085a@5.181.51.80:26656,51ca404bbc73d07fc0d6529388c90f807c5acf0b@65.109.104.72:20756,dfe5f91f824880e19d47475546d9874e0f2cea8c@5.79.74.229:8095,0c38efdc028867765e68f02979958468384ad087@51.89.155.2:23656,8ab347211b90560a0dca64ef0e4eef29012f2f67@65.109.71.119:26656,6c42aacf3939d503bad695d86108d214680e04a8@144.76.175.189:20756,744f2ecd98984eb0e20640ca4b7be69c0be0b81d@45.83.106.141:26656,2e756df28be5e4fa7d332ba732a160202ef86eee@167.235.21.165:26656,6870906f86e474d88d077c7c55af36debe49da04@178.162.165.194:7095,a46ad42b84690a2af0071f20337182b3bfba75fc@38.146.3.130:20756,56a59158450e6f819502812cf28febd65c1ac6be@206.189.26.213:26120,1be5580fb5c50c4225bd0002982816ea9bb2d351@81.0.220.94:24856,59c74642d0ec4d012dd7bd0a7e5af1eadf2061b2@65.109.30.183:26656,a0a450ead908bd65813322c1373802ef32c5736d@65.108.235.33:4000,1285606b577feaed7f045201a67f4a4e38f4726d@65.109.239.8:26656,78f0f5aa89b7ed92a5728dd3f67f646d8dda5213@198.244.228.162:55736,cf75b4e7c27d950181964e99bab6c7aaf330a312@85.214.64.99:26956,6f6f726ae93eadec16ea3de93e147de4061b6be4@84.203.117.234:26656,aedf3405d57c3efdcc2bdb1d571dc10f05247f08@51.89.40.85:22656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.migalood/config/config.toml
```
