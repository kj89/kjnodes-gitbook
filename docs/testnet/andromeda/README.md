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
peers="a14e423bd01f55bdc29c2eeac99aaa0398e94228@45.14.194.212:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,debdccc98a2f6ed72561d7866381003903197935@144.126.142.78:29656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,360ab15495b087bc27d134418dcd9191dec07c12@46.175.148.142:26656,2e6164a7c45c1840494af5db9bc54aacc39a065e@85.239.233.241:26656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,62f7aaafd73816bdaf685a6270541c1d1f8162ad@155.133.27.170:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
