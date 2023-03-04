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

**live-peers** (16)
```bash
peers="7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,2e5ac443db5dc855bb33570ef58ce21cf130197f@82.208.21.15:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,2475bcd6fc1950d8ddecfccd2c3161ce99130741@194.126.172.250:36656,7ff2aaa5c49a0907e52689cc90fa416ec70e06a4@185.245.182.152:30656,433cc64756cb7f00b5fb4b26de97dc0db72b27ca@65.108.216.219:6656,69e89a5169fef99ed1b72dadd4f5c7b801616c88@142.132.209.236:21256,8870aca1936673bb2068ed07fcadc6c46d3ec3a1@146.190.83.6:22656,497f453d42d2db70f0af4ca4acb1f85896bf903d@65.108.200.60:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,d0ef5f5583ff0343ea41962f68010bff54caafde@212.90.121.45:30656,093a6c911937d6d870780003c2b0a39c050d9d85@194.31.109.199:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
