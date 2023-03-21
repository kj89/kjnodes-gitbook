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
peers="63996f52b1dc68259ff64bb2546625c71fc9d546@176.9.48.38:26656,6c0ddab56755cd010f65f1f1201d29120a2d9092@38.242.202.200:31656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,e374d21e689d4e1832ef72e0dae2a9bca435ba36@95.217.114.220:46656,dddc76ca6279ac90b12cf35b39c46a2fc2c2ce52@5.161.78.48:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,6ee2e6550cd3510c0fc912bf0632a894148a79a7@38.242.202.174:31656,22acf9a303e825ce04171ef26e2326c09aeb238b@47.147.226.228:55656,a9444e3bca5023eaaa6b670258bedfa8dcbaf7cf@116.202.170.159:24256,ca2cfea3c48640c094ad740bb41c2aeb81b5dcc6@194.163.187.175:46656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,ed26b4f13a7f388064aa89e5d6419b0e78e3e94e@209.126.81.190:26656,f91eda7a7c64cebd5ad465613b15ea8e8f78aebc@194.163.164.1:26656,0d30a0790a216d01c9759ab48192d9154381e6c0@136.243.88.91:3240,e5fe159e0f035ff4dd8db28a6d6e26703af70d30@104.129.1.74:26656,56e0f891f8312e239a631aea2f8b0e64c9f7d824@135.181.95.145:36656,998b19ed2c580acaa2fdb5057e2930a38f041750@65.109.122.105:60556,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,140d07c40c964eb063d4526561ca92e8ed796b9b@65.109.82.249:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
