# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: andromeda-testnet.grpc.kjnodes.com:47090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:47656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:47659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (30)
```bash
peers="e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,4d4309bf054ca12f128035eab81b66350b5de575@178.172.212.122:26656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,a4d291d17d8e74979e7db5a1e936269835e802af@194.165.59.78:26656,6665e836cfe7ca1cfcc2e056fc9ed5400511af72@45.132.106.161:26656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.12.196:26656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,ef6ec2cf74e157e3c6056c0469f3ede08b418ec7@144.76.164.139:15656,dfa4155254cf862fbd411b9e02e26ecb00cd2436@85.10.198.171:26456,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,704e605f9bd65912d8c65a58f955601c31188548@65.21.203.204:19656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,832f366a1429db31ca6cca1b134f304daacbb302@82.146.41.203:26656,00c49b6c8f0613bda77f27bf5072e4a000ace2b7@89.252.21.37:60556,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,03dc9e3ec16856653e0361f290a7580cf6b26a86@65.108.66.34:29556,de8e1fd6c53fa464965b547d100f091277ddcb04@80.89.229.115:26656,6aaf94803e3f387a3ee08b731890e6914e1e3419@65.108.233.102:30656,f065bd4154e33dad9b6ca3e04bf3f8a9bcab9567@1.53.241.61:47656,e8f8c97c65b3e65797eca3489de7c1682e85d4df@78.25.143.46:47656,1141119a7d248cc19b31b18d56162a365954deb9@45.132.106.149:26656,257491189415103312bcd203b1c6cd114d2cde9e@38.242.225.252:26656,855a1da5a4dc8381804b4a76158a69f41397447c@212.227.12.83:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
