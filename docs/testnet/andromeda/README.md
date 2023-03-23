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

**live-peers** (13)
```bash
peers="bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,3969b8ddc6d0ed9f2deb0265e4b26e88c5cb894a@149.102.150.250:30656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,bcef415d908dfc5c7caff3325eefd51a730695b4@65.21.92.46:30656,62f7aaafd73816bdaf685a6270541c1d1f8162ad@155.133.27.170:26656,cc1c2cd585792d81a041e9098e36814dc8d1e6ae@213.239.207.165:28756,95e8225c5b8a21c1fecd411f37c75f5515de1891@185.197.251.203:26656,29a9c5bfb54343d25c89d7119fade8b18201c503@209.34.206.32:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
