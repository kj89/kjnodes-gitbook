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
peers="6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,c9dc9d0ddcd9aba39353c77f03168a85912849e3@65.108.200.40:33656,fb124c136c3aa20a71c68d9cb0a2833293c8dc58@23.88.73.158:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,9446504166663fc0090b81abdf86fafe93e72a40@185.209.30.95:40656,a79130668102f116a23cfcf9fd94623de4a223fe@81.30.157.35:10656,2788c4e5178166010baf8786ad3091a9fcc1a730@5.78.101.216:26656,33527195a479780ce40322433f1eca5d11bc47f5@89.163.140.70:26656,7b1f3e49e2a21e59e11e434e3bb8907d4d3705d1@65.21.202.160:13656,acad4439671fef4e64e904587a81ee9c34e9505d@95.216.214.103:40656,8fdba2d059cdae2e9560ce817c1cd024b2747205@65.108.133.103:26656,c1c6cf5859c43fb3acd19ccdb78a4caa0a151ff7@45.85.249.107:27656,73a560b069d3ab8991ff83a8d2f3453d891e05c6@92.55.63.130:32656,bda598af0c96d72a85c3b6840138d929b8c4e762@84.46.248.207:26656,0537a8d627b65f65c810206dffef9fa820183167@65.109.160.32:40656,ee5ad3b44e90903d0bcecdbc0b4f16c4a3fa73d3@83.167.103.215:26656,23c52b4aa95a5b269277292410f6f4c8815e616c@194.163.174.103:27656,86caf6297ae00fb58b58a272984275c592b2fdf7@65.109.84.216:56656,fc8ad183d32ca52eabc2d3af8e1e85b06ca1286a@159.89.117.7:26656,250533acd9a86a23e5d5c6206465cec08ea48fca@195.2.80.176:26656,16b5afa82d6cde08c1add89bb0c445e707aed9ed@88.198.57.88:26656,1b16614a7f8c703db882dc44095c12c9e4d21900@89.163.240.178:40656,6b94a3f12d8e694c3a735078e0cfa2b27940012a@95.214.55.62:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,aa3878e41e692cd7530387d94fd02012dd025b40@135.181.93.86:40656,185401b61cbe26895b5a7c025e8666349c3129ff@213.133.97.154:13656,cdcd6ba08042b31391492666da593cc80d198cab@84.54.23.85:26656,22fa766ffe457fd1236ea88bce1f40bf4bbaf328@77.91.100.131:26656,288bafc7978c4e9adee447a06b97de11c87c7227@185.202.238.250:26656,8a5cc818253b02eb408314ea1b5ff4788cc6e7a1@65.109.65.248:33656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
