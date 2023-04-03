# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.2.2 | **Wasm**: ON

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

**live-peers** (28)
```bash
peers="e0ab3276d94a8fbdf04b0b9eb95df22f7037eb89@167.235.31.186:34656,6cb8e63bf00d37399454ab24b6cf316062b90117@199.175.98.110:36656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,50d786a2d242839fe2bdb69bee694d7ffa455824@5.161.60.42:18656,46e87e63ebfb628613a7c33ff69946ebd45fa510@176.99.142.180:36656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,654e76e7d4b27fdb3a931fe2d44c51184d8a5731@5.161.78.48:26656,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,fac035258738be9be98957d5d012d24841d2e5eb@85.10.197.4:16656,441ee01f2bb396bf4116f197e4d9eefbd88f5e10@65.109.122.105:60756,72ccd1176df36fb799e14721639e21b1ec360f0a@65.108.9.164:20756,fa0a2fe57c2ab28aee6cc0be4eddbc68d6587a75@95.217.165.189:26656,3a0ca1d94b199af43ae28d32572dda8c5cc723d0@15.235.114.158:26656,4d8aed7bff4156c62ebb4f787e06d5d45d681b76@109.111.160.171:34656,cd67fc6e6c306dbb863f381c926135d6b97fe685@65.109.85.155:41656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,4c70dbb030c7b38e8f16999787074ed5ae33ba0a@94.250.202.17:26656,38e75806248cd215e1e71d94e3db8c08bcf87702@95.214.55.138:27656,cdfcaee60fe31b33a32929a3e15d02f8e2508f98@135.181.160.61:31656,b7d04a32d5c0e9b7e1095c4d81f5bebfd03138db@65.108.8.28:61456,c86c29f1118891b1543c14f5833e6f26e9231a10@213.246.39.53:36656,5d323e4127ebf0c3139f3081765606e32052fa3e@65.109.92.148:26656,43b2582d9f63b46df12879729e8d3d1daa899ef4@144.126.154.230:26656,1825de8cabc89fddea10f1cf9d65eda46b0cc7a1@5.9.121.55:41956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
