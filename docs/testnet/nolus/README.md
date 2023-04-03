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

**live-peers** (27)
```bash
peers="ee7579d3dadb725ce0ed1e453fd72c2fcbb7b9af@142.132.208.26:26356,e0ab3276d94a8fbdf04b0b9eb95df22f7037eb89@167.235.31.186:34656,538e2a3d6e96cd7bc0635eaa3f8f3695f26503a7@65.108.104.167:21656,fac035258738be9be98957d5d012d24841d2e5eb@85.10.197.4:16656,ca83b6457bfce88d892646b6afb51165ec3e94d4@135.181.183.93:22656,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,fa0a2fe57c2ab28aee6cc0be4eddbc68d6587a75@95.217.165.189:26656,8d85b69ea7175ce0cf6ec7badae239339d6525db@81.0.218.59:26656,e4b7228ccadf3180e6e323aa4c0c97946ac054dc@65.109.112.20:11134,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,b7d04a32d5c0e9b7e1095c4d81f5bebfd03138db@65.108.8.28:61456,1c50df97e155afa50189f48daf41be046c7fe682@85.10.202.135:32656,58d7fc67e12548f3f1ddda3bbe6000ae3d9d638c@85.10.198.169:13656,654e76e7d4b27fdb3a931fe2d44c51184d8a5731@5.161.78.48:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,84a5abdf6ce6f573ac1e3086ca693da6ec17c244@84.46.246.79:26656,6cb8e63bf00d37399454ab24b6cf316062b90117@199.175.98.110:36656,46e87e63ebfb628613a7c33ff69946ebd45fa510@176.99.142.180:36656,f50302cde48497a2af29168c23c530299116fd84@89.252.21.37:36656,72ccd1176df36fb799e14721639e21b1ec360f0a@65.108.9.164:20756,9f7560998c1bbced14d48261360746ce6cd09ec0@93.100.234.251:16656,38e75806248cd215e1e71d94e3db8c08bcf87702@95.214.55.138:27656,5d323e4127ebf0c3139f3081765606e32052fa3e@65.109.92.148:26656,441ee01f2bb396bf4116f197e4d9eefbd88f5e10@65.109.122.105:60756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
