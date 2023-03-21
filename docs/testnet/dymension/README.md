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
peers="56e0f891f8312e239a631aea2f8b0e64c9f7d824@135.181.95.145:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,1135bf4bf8ffad1b9b508ea6c7408085ec87563a@134.122.16.44:26656,1bffcd1690806b5796415ff72f02157ce048bcdd@144.76.67.53:2580,22acf9a303e825ce04171ef26e2326c09aeb238b@47.147.226.228:55656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656,f91eda7a7c64cebd5ad465613b15ea8e8f78aebc@194.163.164.1:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,140d07c40c964eb063d4526561ca92e8ed796b9b@65.109.82.249:29656,eb524a9ed0e080ec4fa9a21df3f5f56e94e0e811@51.89.7.235:26652,b8d08951d68da03af8f9272bf77684811197c289@95.216.41.160:26656,e374d21e689d4e1832ef72e0dae2a9bca435ba36@95.217.114.220:46656,64acca240c1149f94b8986ffea3ee1b4e0bd5fbe@45.150.64.115:26656,c36184fec2fb60bf7be775390c1cd6619c0201ef@209.126.81.240:26656,e5fe159e0f035ff4dd8db28a6d6e26703af70d30@104.129.1.74:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
