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

**live-peers** (29)
```bash
peers="94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,ce64cd3050be198f6fe0d59cd4333b40aedcfc2f@14.241.82.87:28656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,2e6164a7c45c1840494af5db9bc54aacc39a065e@85.239.233.241:26656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,e95899eb682e517d74449dd575073daf1a3266d5@135.181.208.169:27656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.12.196:26656,eec703fc2d5e7c1bbd81726a9e029dbb8b6221b5@178.250.247.119:26656,b2bdcd106645c538f86f24f7a3f253d8e1bf34ab@217.76.57.54:26656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,7002fb6369cd13f8aa1520fd7a81e67a9adf2636@185.119.196.39:26656,c6f2ebd60d3e8bb559bdf866356fea0711df223d@82.208.23.192:26656,4d4309bf054ca12f128035eab81b66350b5de575@178.172.212.122:26656,1141119a7d248cc19b31b18d56162a365954deb9@45.132.106.149:26656,049cb9d4376556e28da12171bcba5f58cb8eaabb@185.202.238.250:26656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,0a9c34419331688b0b40d50fddbee286927602cb@5.78.79.97:26656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,f58c0d432b28ebefb7573ab23cb394e67098c347@209.126.81.240:26636,6aaf94803e3f387a3ee08b731890e6914e1e3419@65.108.233.102:30656,42741bf91bce301f78660db6cc385fcfaac91498@173.249.47.194:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
