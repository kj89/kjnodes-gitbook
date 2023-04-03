# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.2.1-testnet | **Wasm**: ON

[Website](https://www.nolus.io) | [Discord](https://discord.gg/nolus-protocol) | [Twitter](https://twitter.com/NolusProtocol)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nolus-testnet](https://explorer.kjnodes.com/nolus-testnet)

## Public endpoints

* api: [https://nolus-testnet.api.kjnodes.com](https://nolus-testnet.api.kjnodes.com)
* rpc: [https://nolus-testnet.rpc.kjnodes.com](https://nolus-testnet.rpc.kjnodes.com)
* grpc: nolus-testnet.grpc.kjnodes.com:43090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nolus-testnet.rpc.kjnodes.com:43656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nolus-testnet.rpc.kjnodes.com:43659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nolus-testnet/addrbook.json > $HOME/.nolus/config/addrbook.json
```

**live-peers** (30)
```bash
peers="acd39ab5b00e5611df296b2e6fb4f6a44a32513f@23.88.5.169:21656,b19bd98f29fefc0c78e6b16b02e652a2148d3bfe@91.223.3.144:26556,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,6cb8e63bf00d37399454ab24b6cf316062b90117@199.175.98.110:36656,b7d04a32d5c0e9b7e1095c4d81f5bebfd03138db@65.108.8.28:61456,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,fac035258738be9be98957d5d012d24841d2e5eb@85.10.197.4:16656,e8473dede42e7f0d4668a24d909a5708c5a04a3e@65.108.78.116:11656,6b14535ff005667f324f8439a55a21ee2f170d12@95.217.211.81:26656,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,e6e48680fa62c03bed242c52eb21d3cbe44a6752@46.8.210.144:26856,50d786a2d242839fe2bdb69bee694d7ffa455824@5.161.60.42:18656,367fb20ca2380ebbb73eb19b772564383b0f37ee@65.21.123.172:26656,f50302cde48497a2af29168c23c530299116fd84@89.252.21.37:36656,d8088d91bdbf2ccdf59f0b3ee1c1b07e8cb60798@195.201.237.185:11656,441ee01f2bb396bf4116f197e4d9eefbd88f5e10@65.109.122.105:60756,72ccd1176df36fb799e14721639e21b1ec360f0a@65.108.9.164:20756,cd67fc6e6c306dbb863f381c926135d6b97fe685@65.109.85.155:41656,5d323e4127ebf0c3139f3081765606e32052fa3e@65.109.92.148:26656,ac86c1678e20a87bf2f036741932910869726337@135.181.222.185:15656,8d85b69ea7175ce0cf6ec7badae239339d6525db@81.0.218.59:26656,4c70dbb030c7b38e8f16999787074ed5ae33ba0a@94.250.202.17:26656,a95975f3a58e20ba1c518f3cbb1c23ef7569e4d4@14.241.82.87:26656,05ce20b26a95b9360896d24c330a7b421bc13805@194.163.174.222:26656,22acc593150fc38f9b1a2dc93cdc05e22566e7f6@213.239.207.165:29856,1825de8cabc89fddea10f1cf9d65eda46b0cc7a1@5.9.121.55:41956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
