# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: orbit-alpha-1 | **Latest Version Tag**: v0.2.6 | **Wasm**: ON

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/defund-testnet](https://explorer.kjnodes.com/defund-testnet)

## Public endpoints

* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)
* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* grpc: defund-testnet.grpc.kjnodes.com:40090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (30)
```bash
peers="7d9853992a3ce9a88d5e052c333bddf99d923b82@86.102.123.237:18656,2da5c563e31d3f3a0101f55ec6186d65465881d9@95.217.88.248:13656,e3c348467a8c88c0f65e2ca8a71875d2a384b8b4@185.16.39.19:60656,70c35e37f399fe02d41823c97188a4e5911d5b17@38.242.217.231:26656,6b94a3f12d8e694c3a735078e0cfa2b27940012a@95.214.55.62:26656,ed3c51ed404d9ea1ea7ce4c457430cc15b127fd0@38.242.232.172:26656,ccdcb9537831ddff0ce70d42fa056baf7d60549b@148.251.8.6:13656,94b85ff9d2b522296bd6fef58c81cba81619aa3e@155.133.22.130:26656,11c0952beaf78a6452d270c7bd344c25406e1b16@95.217.212.66:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,fb124c136c3aa20a71c68d9cb0a2833293c8dc58@23.88.73.158:26656,33527195a479780ce40322433f1eca5d11bc47f5@89.163.140.70:26656,9afc6f16f21823d3850f5d18f66de786ea9ecea5@94.130.218.86:13656,fc8ad183d32ca52eabc2d3af8e1e85b06ca1286a@159.89.117.7:26656,1ff43841e4395dca585678be6a790df9a037f1cd@209.38.252.86:26656,70a72a3fdec5195882e99abd023badce1548d9c9@155.133.22.134:26656,73657fd476a5a21f74e2f9d61ddc24709035b9c2@65.108.209.237:40656,789f5035190704fac04402363713179cb6c6ad00@109.195.139.31:26656,bda598af0c96d72a85c3b6840138d929b8c4e762@84.46.248.207:26656,6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,86caf6297ae00fb58b58a272984275c592b2fdf7@65.109.84.216:56656,a56c51d7a130f33ffa2965a60bee938e7a60c01f@142.132.158.4:10656,72fec183abd9e39d95970f2b9483b66e8fe3c25e@155.133.22.136:26656,002422812948a68fe851bed557de2d0040d41e06@31.220.80.134:30656,0108df8793ec07fa82ea202d54b70c603b827ea4@5.9.81.251:60656,34b72721aa503574a0709b1859fb1da2aa12ce70@88.99.3.158:11256,875c807628a014aff8b4cdcbd812f183a0338d42@91.107.204.206:26656,f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
