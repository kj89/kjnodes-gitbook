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
peers="bccd2003a7eb23008479c76427ac2c276160e09a@75.119.154.72:26656,5ce286faea0eb730e6d4f3636ab572fea20a879d@86.48.5.92:27656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,70a02b29719f2a3f7347e03aac2681af6c634f33@158.220.100.181:40656,3e5d4205a82d9e5ed82ca8f4d0adb57522edb74e@65.108.72.233:06656,eb7040eb80f3a0b62df828d38d818b3aec554b50@38.242.237.125:26456,7cf6dc70e9dfa82db373120de0d79dddc71bd74e@194.34.232.99:26656,23c52b4aa95a5b269277292410f6f4c8815e616c@194.163.174.103:27656,06c0fe8a5df43f71e88eaa3c07891338026ade9b@193.34.217.164:26656,743e36f7e5e7c12cfd1e7951a69a7283ac3c625f@93.183.211.205:26656,90f293a5f20979c5778ba6156597e7b9eb04539b@93.183.211.204:26656,82ac9dfeff1c46a985c6680022288e36aeb12ac3@65.108.40.28:61056,11d29b833c759f5595ffdb5d0652890a8972e0bf@185.217.126.168:27656,3500e23aceb48039d45f7d3f31869c71202f6519@194.163.169.45:26656,55ab73ef10e4b6e6c98564df29565829cf12673a@65.108.159.127:26656,33527195a479780ce40322433f1eca5d11bc47f5@89.163.140.70:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,dd21f9f7d9559653f3713ab32893a025c1075d28@65.108.234.26:27656,7a3c4079964eaca46f63f9a4ba37997ae55bee60@45.85.249.93:27656,ffb2898494cdbd6625d962ea4511c29507177c62@164.68.103.176:26656,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,6ebc61d0765449b67645339e0b85f1f7fc0b5955@38.242.141.23:36656,f8036fa5e78f72606209d8022905a96364b82d19@185.209.230.110:27656,0537a8d627b65f65c810206dffef9fa820183167@65.109.160.32:40656,0e191c0d1fed5e6745bee750309a9730beacd667@178.239.197.171:26656,4f1d96f5b8adb5bcdd59e61cb6e387ff12422a41@65.109.63.110:13656,875c807628a014aff8b4cdcbd812f183a0338d42@91.107.204.206:26656,bd36a3e46bad265ebb1a0c05876710aff8b2db9e@176.124.222.160:40656,6047d282f126e8be4b36ca28c0cc3d244577f798@159.69.185.109:26656,af9f3f65b3082007020697d035e7d5031e3be25b@212.23.222.89:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
