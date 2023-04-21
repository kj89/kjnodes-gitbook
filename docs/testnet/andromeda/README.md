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
peers="54188a9dea5ded1d891aa6c3c0e2a403322b1707@178.54.78.180:16656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.12.196:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,1141119a7d248cc19b31b18d56162a365954deb9@45.132.106.149:26656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,0a9c34419331688b0b40d50fddbee286927602cb@5.78.79.97:26656,f66bcec970aaaaa9ae33182802ac4bf87b3b20cd@84.46.254.82:26656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,69e89a5169fef99ed1b72dadd4f5c7b801616c88@142.132.209.236:21256,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,c45d01b216a7f24a06448a47b6cf19a42e74c29b@65.21.170.3:32656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,e95899eb682e517d74449dd575073daf1a3266d5@135.181.208.169:27656,ce64cd3050be198f6fe0d59cd4333b40aedcfc2f@14.241.82.87:28656,7649ae1ea0dd5f640ac7dd7632a0866cf65e3aa4@31.220.90.78:26656,eec703fc2d5e7c1bbd81726a9e029dbb8b6221b5@178.250.247.119:26656,ef8045e2922cf856b73f5fa5efdb79f925204ccf@65.109.117.159:15656,1c9d70cda1b46e8a33a39783e9af0ad8b5d876ac@65.109.85.225:3340,bcef415d908dfc5c7caff3325eefd51a730695b4@65.21.92.46:30656,011c1c98fb63b99e8fd2aaf8a02f60cd45154179@45.132.106.178:26656,5cfce64114f98e29878567bdd1adbebe18670fc6@65.108.231.124:30656,85953732c4eb5165724ac6db331240ff0815daf1@1.15.104.210:26656,717066f5726fb3cd7096f84911c7c8bfe5953e62@81.68.158.68:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
