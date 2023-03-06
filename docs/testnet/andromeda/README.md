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

**live-peers** (17)
```bash
peers="a14e423bd01f55bdc29c2eeac99aaa0398e94228@45.14.194.212:26656,2e6164a7c45c1840494af5db9bc54aacc39a065e@85.239.233.241:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,c45d01b216a7f24a06448a47b6cf19a42e74c29b@65.21.170.3:32656,03603fb96ded3aabe7451efad31fb8d0c523a0ee@146.19.75.97:26656,4cd929e58c35970289659e402a582115671baaee@65.109.106.91:25656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,093a6c911937d6d870780003c2b0a39c050d9d85@194.31.109.199:26656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656,e2efe3e1d7e0ed2e5b6a1b384c47f745e9f205ac@65.108.141.109:31656,bb81a52f86a5332e447373796f8a0b99f195816d@5.78.67.243:26656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,c66e5cc02d87731faf781463466bf39723d4558b@68.183.181.120:26656,0aed895e88d792e71968a18fc70fbcd62a997f99@65.108.232.238:15656,2475bcd6fc1950d8ddecfccd2c3161ce99130741@194.126.172.250:36656,f1bca379ca2f358ddb39a69fdb0c9755903aeba8@80.76.43.138:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
