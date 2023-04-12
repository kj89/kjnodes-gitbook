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

**live-peers** (23)
```bash
peers="ee7579d3dadb725ce0ed1e453fd72c2fcbb7b9af@142.132.208.26:26356,654e76e7d4b27fdb3a931fe2d44c51184d8a5731@5.161.78.48:26656,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656,8d85b69ea7175ce0cf6ec7badae239339d6525db@81.0.218.59:26656,46e87e63ebfb628613a7c33ff69946ebd45fa510@176.99.142.180:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,b0fa31de7a29b92b4c910cbafb2789626a1db8a9@65.108.9.164:20756,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,003a270b5085d8c14a075abc1ac3699f34161e49@185.248.24.224:37656,f9734a35578309156308f12eba510ef995de4769@165.22.111.173:20756,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,87e0efe332fdc4b0c2a76d18761a936509762067@212.41.9.98:36656,50d786a2d242839fe2bdb69bee694d7ffa455824@5.161.60.42:18656,e0ab3276d94a8fbdf04b0b9eb95df22f7037eb89@167.235.31.186:34656,d8088d91bdbf2ccdf59f0b3ee1c1b07e8cb60798@195.201.237.185:11656,2e80da0046dd3f2205a207dd435b6c9b0f9bfc04@65.109.93.152:27656,5d323e4127ebf0c3139f3081765606e32052fa3e@65.109.92.148:26656,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,e6e48680fa62c03bed242c52eb21d3cbe44a6752@46.8.210.144:26856,22acc593150fc38f9b1a2dc93cdc05e22566e7f6@213.239.207.165:29856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
