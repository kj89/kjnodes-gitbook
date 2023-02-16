# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: OFF

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/andromeda) | [Twitter](https://twitter.com/andromedaprot)




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
peers="dfa4155254cf862fbd411b9e02e26ecb00cd2436@85.10.198.171:26456,df7cf95427701d6d00797042fb8548a7f8eeeb6e@172.104.159.69:55716,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,4cd929e58c35970289659e402a582115671baaee@65.109.106.91:25656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,f51b215535e43428b7122c3d3ebbb4ab20c1b808@185.9.144.138:26656,497f453d42d2db70f0af4ca4acb1f85896bf903d@65.108.200.60:26656,0aed895e88d792e71968a18fc70fbcd62a997f99@65.108.232.238:15656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,8a551bc0cc7ba190db9126c8fc95c8b643ae511c@195.201.174.109:56656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
