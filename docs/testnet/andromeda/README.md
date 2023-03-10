# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)




## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: [https://andromeda-testnet.grpc.kjnodes.com](https://andromeda-testnet.grpc.kjnodes.com)

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

**live-peers** (12)
```bash
peers="8cac168380851851b9318a2176dca8fb690e26d2@95.216.7.169:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,f1d30c5f2d5882823317718eb4455f87ae846d0a@85.239.235.235:30656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,8083dd301a7189284bf5b8d40c4cf239360d653a@5.9.122.49:26656,19f9022eb4d36164288deec5b0badc1ba2e9a1af@89.163.164.110:26656,debdccc98a2f6ed72561d7866381003903197935@144.126.142.78:29656,bcef415d908dfc5c7caff3325eefd51a730695b4@65.21.92.46:30656,2e6164a7c45c1840494af5db9bc54aacc39a065e@85.239.233.241:26656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,bb81a52f86a5332e447373796f8a0b99f195816d@5.78.67.243:26656,086dd26d09ee6ff66307555cb9a25e0df76f377f@65.108.199.206:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
