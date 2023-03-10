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

**live-peers** (14)
```bash
peers="bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,debdccc98a2f6ed72561d7866381003903197935@144.126.142.78:29656,f1d30c5f2d5882823317718eb4455f87ae846d0a@85.239.235.235:30656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,8cac168380851851b9318a2176dca8fb690e26d2@95.216.7.169:36656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,0a9c34419331688b0b40d50fddbee286927602cb@5.78.79.97:26656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,e2efe3e1d7e0ed2e5b6a1b384c47f745e9f205ac@65.108.141.109:31656,19f9022eb4d36164288deec5b0badc1ba2e9a1af@89.163.164.110:26656,50ca8e25cf1c5a83aa4c79bb1eabfe88b20eb367@65.108.199.120:61356,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,08da04e20e295f48518d095871ba5c13e58c3dfd@185.209.223.64:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
