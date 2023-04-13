# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/migaloo.png" width="150" alt=""><figcaption></figcaption></figure>

The Migaloo chain is a permissionless Cosmos SDK chain on which  projects are encouraged to build their applications. Migaloo chain  is the home of the White Whale dApp, Interchain Command Center.

**Chain ID**: migaloo-1 | **Latest Version Tag**: v2.0.1 | **Wasm**: ON

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
peers="7e2bf7bdcc3b40a1dae4c9befb1ef1cb47d03c6d@65.108.10.37:26656,ccaccdf6bafcb57197d86a1420a289cd39fe0ae9@85.10.200.231:8095,dfe5f91f824880e19d47475546d9874e0f2cea8c@5.79.74.229:8095,59c74642d0ec4d012dd7bd0a7e5af1eadf2061b2@65.109.30.183:26656,e91f650bb3d5b66762093150718af358c6355cc5@15.235.10.35:36656,80be85c4980deccaa2fbd710029f0eb660dadf9a@51.81.16.186:26656,4236750928a4dcb742e50e30e500ebc9ee39f240@35.223.246.103:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:49656,70d1818f50d983bfebf4c8546b221687b76cd4b0@51.81.107.95:20756,fe04ff9a13d8f0b23463e832f75eb5c845bd375e@213.239.214.73:7095,2fd235d3f0a1a84abd197dcfdaf04fdabc092db8@168.119.62.80:26656,3b3428d679faa1bd498b3554ca798de3a0d802c6@162.19.89.8:20756,347e6fa3c974e91aee92da5793486ba3f1bae67d@23.88.112.67:26656,0326c9ee117587b7ebe3b26b00820642a8cf48ff@65.108.238.102:20756,aba0c3f98fb5bef1a0d991b8e2b8bba24f9908b6@65.108.111.236:55736,554eb4a15e05af8317c3f98d6efd51d1ace1bc9c@146.59.85.223:20756,f7dede5bd05eb9615c8c6fa273e25bd4f10f56b8@65.108.109.240:3000,8a9e42026a687b2762cefbd74584ccbd6afa0be1@65.109.83.124:26656,0c38efdc028867765e68f02979958468384ad087@51.89.155.2:23656,2e71dbd7d4c079ba7894c5287291c17ba58a6504@141.95.47.78:26656,6870906f86e474d88d077c7c55af36debe49da04@178.162.165.194:7095,462a37ca052c4d058e505959393574045dce9489@116.202.36.240:20756,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27096,dfb44159d26b62affd7112367e082b2397bbff15@65.108.136.206:26656,c616069071f0864b5b0e995f8d8961536b41ab62@15.204.141.36:26656,9cb7ba30c7eb7e9b516b90e09ca0f53250927440@146.59.52.135:8095,95a68d5280d9a3ae6d688e89bd4e4fe295b11a92@31.156.88.34:26656,6c42aacf3939d503bad695d86108d214680e04a8@144.76.175.189:20756,a834ef7ec0a65ac7c5bf976a9af5adb3a71d7a19@65.108.8.247:20756,9780ea85f4d0f4cb5ebca14992ce11ebe1982d35@188.172.229.26:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.migalood/config/config.toml
```
