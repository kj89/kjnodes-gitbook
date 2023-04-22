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
peers="7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,3f9594221efe3e9cd4d0de31f71993fc0f12bf01@65.21.245.252:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.12.196:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,d3ac63ff921486f8aef1eba7870cae1d14c38633@1.15.146.92:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,9e14886f7a34c73e65eafb209a9215e2848e9e76@65.108.41.172:29456,38a626dfc05c0d9756098349ce8ccd532496d6a2@65.108.206.118:61456,7c9e768cdaa68d5c27b49797284acbd9d0dd9716@79.137.248.65:26656,53d6083066936978f86feba4d9cc700ac0e65e9f@178.172.212.176:26656,a39aac2e81ec23b639c5ed86273fcf80701187a7@5.182.36.198:26656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,1141119a7d248cc19b31b18d56162a365954deb9@45.132.106.149:26656,f66bcec970aaaaa9ae33182802ac4bf87b3b20cd@84.46.254.82:26656,fd48e41b990c9ba2cdd3e2f5adf20b8ab237b328@1.15.110.177:26656,eec703fc2d5e7c1bbd81726a9e029dbb8b6221b5@178.250.247.119:26656,ce64cd3050be198f6fe0d59cd4333b40aedcfc2f@14.241.82.87:28656,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,ef8045e2922cf856b73f5fa5efdb79f925204ccf@65.109.117.159:15656,9939a8f08849b1d77b1bd5f5033d6ce9ff7a20f5@49.12.234.38:20656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,8870aca1936673bb2068ed07fcadc6c46d3ec3a1@146.190.83.6:22656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,505b62b16c6e11f6cced2f3f8283d08862bdc822@164.90.208.147:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
