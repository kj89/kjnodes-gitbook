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

**live-peers** (12)
```bash
peers="3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,4cd929e58c35970289659e402a582115671baaee@65.109.106.91:25656,2e6164a7c45c1840494af5db9bc54aacc39a065e@85.239.233.241:26656,4d4ef8f6ff2f1ac8ba5e102e858f6ecbd0d3dda1@31.220.84.3:26656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,c45d01b216a7f24a06448a47b6cf19a42e74c29b@65.21.170.3:32656,0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656,62f7aaafd73816bdaf685a6270541c1d1f8162ad@155.133.27.170:26656,8870aca1936673bb2068ed07fcadc6c46d3ec3a1@146.190.83.6:22656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
