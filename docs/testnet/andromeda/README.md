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
peers="815e9378b05a40e4a774223b55f5c6b8457a1c79@31.220.79.166:26656,c45d01b216a7f24a06448a47b6cf19a42e74c29b@65.21.170.3:32656,c89e274523cec4a7445afaff1ab35029b090ff5b@65.109.116.204:20156,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.21.244:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,c4bb11ae43f4db7b8eef312a3c38861d236eb660@91.201.113.194:26656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,1141119a7d248cc19b31b18d56162a365954deb9@45.132.106.149:26656,ef8045e2922cf856b73f5fa5efdb79f925204ccf@65.109.117.159:15656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27126,cc1c2cd585792d81a041e9098e36814dc8d1e6ae@213.239.207.165:28756,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,28ce2dfb6c76e0baa660ec647bafe4a3b88cb3b0@94.131.118.190:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,ce64cd3050be198f6fe0d59cd4333b40aedcfc2f@14.241.82.87:28656,537e0302400604f7dd1b8e49c5660da311066610@199.175.98.104:26656,0a9c34419331688b0b40d50fddbee286927602cb@5.78.79.97:26656,7002fb6369cd13f8aa1520fd7a81e67a9adf2636@185.119.196.39:26656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,7469fd307adba5d8e782908ee01f080f3e554c48@185.154.13.19:26656,62f7aaafd73816bdaf685a6270541c1d1f8162ad@155.133.27.170:26656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,b24f0d76009c9d0b0492694caa6d913feb3ad2b0@38.242.255.3:47656,8f009df7a9394c19c0aa3a84f129baacb66b7009@82.208.21.242:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
