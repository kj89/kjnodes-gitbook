# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/dymension.png" width="150" alt=""><figcaption></figcaption></figure>

Dymension is a network of modular blockchains called RollApps  and at the center of it all is the Dymension Hub. Dymension  allows anyone to build and deploy their own consensus-free blockchain, a RollApp.

**Chain ID**: 35-C | **Latest Version Tag**: v0.2.0-beta | **Wasm**: OFF

[Website](https://dymension.xyz/) | [Discord](https://discord.gg/dymension) | [Twitter](https://twitter.com/dymensionXYZ)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/dymension-testnet](https://explorer.kjnodes.com/dymension-testnet)

## Public endpoints

* api: [https://dymension-testnet.api.kjnodes.com](https://dymension-testnet.api.kjnodes.com)
* rpc: [https://dymension-testnet.rpc.kjnodes.com](https://dymension-testnet.rpc.kjnodes.com)
* grpc: dymension-testnet.grpc.kjnodes.com:46090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@dymension-testnet.rpc.kjnodes.com:46656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@dymension-testnet.rpc.kjnodes.com:46659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/dymension-testnet/addrbook.json > $HOME/.dymension/config/addrbook.json
```

**live-peers** (20)
```bash
peers="ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,63996f52b1dc68259ff64bb2546625c71fc9d546@176.9.48.38:26656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,22acf9a303e825ce04171ef26e2326c09aeb238b@47.147.226.228:55656,998b19ed2c580acaa2fdb5057e2930a38f041750@65.109.122.105:60556,5d689e09a129c03c003f05850262f03b2433a384@51.79.30.141:26656,54160abe97cd71abb3a83516fd8e4a47cb509fba@188.34.178.103:46656,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,e374d21e689d4e1832ef72e0dae2a9bca435ba36@95.217.114.220:46656,ed26b4f13a7f388064aa89e5d6419b0e78e3e94e@209.126.81.190:26656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,1bffcd1690806b5796415ff72f02157ce048bcdd@144.76.67.53:2580,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,f91eda7a7c64cebd5ad465613b15ea8e8f78aebc@194.163.164.1:26656,0d30a0790a216d01c9759ab48192d9154381e6c0@136.243.88.91:3240,56e0f891f8312e239a631aea2f8b0e64c9f7d824@135.181.95.145:36656,140d07c40c964eb063d4526561ca92e8ed796b9b@65.109.82.249:29656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,617214edc6dbd3d82765d66767ca56deb9660851@134.209.21.58:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
