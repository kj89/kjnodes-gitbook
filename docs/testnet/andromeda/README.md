# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (10)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,749114faeb62649d94b8ed496efbdcd4a08b2e3e@136.243.93.134:20095,29a9c5bfb54343d25c89d7119fade8b18201c503@209.34.206.32:26656,0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,a478235ecd296f14a2889fac5eb4b43e5e98c239@159.69.64.22:16656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,c45d01b216a7f24a06448a47b6cf19a42e74c29b@65.21.170.3:32656,c5f6021d8da08ff53e90725c0c2a77f8d65f5e03@195.201.195.40:26656,debdccc98a2f6ed72561d7866381003903197935@144.126.142.78:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
