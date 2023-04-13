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
peers="11c0952beaf78a6452d270c7bd344c25406e1b16@95.217.212.66:26656,8a650a9761db8abc1096abc3d4a68431600ae835@62.171.149.101:46656,c24e38e2bf28f81a6935110c07cdeb95f5765ed1@65.109.84.254:26656,bb427e04d3d7fea5d7afbef5a4ccf3f25840a327@65.21.226.159:13656,ffb2898494cdbd6625d962ea4511c29507177c62@164.68.103.176:26656,cdadad3c8fc2982484fe7fd4fd041dcd437c6f8e@116.202.225.84:13656,86cf7d0916950d2b48294ed6106f045a7b25aec7@77.105.137.135:26656,54315866e9a9c0bd7611a42a1caaf4a244316eb3@65.108.200.60:13656,b0ee2c3fdfb915964c50e5ce2c23077bb3673a52@176.31.138.196:40656,86caf6297ae00fb58b58a272984275c592b2fdf7@65.109.84.216:56656,bc934501cffc27940d96e7775b6b8ae5122604ab@185.185.80.195:28656,cbfc6051bb09df27181ee9e188d9bd9ee4264997@173.249.48.76:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,002422812948a68fe851bed557de2d0040d41e06@31.220.80.134:30656,eb7040eb80f3a0b62df828d38d818b3aec554b50@38.242.237.125:26456,205f6826808509bb8be87bfff953dd422bfff962@207.180.254.16:28656,c9dc9d0ddcd9aba39353c77f03168a85912849e3@65.108.200.40:33656,1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656,04ff1f98174b35960d8bc2d10bf0da1406f7028b@194.146.12.215:27656,1a8e8d6667615f4836c1c1403563a26a1044fd00@116.203.158.189:26656,078860dec222438ab648ced23893dbaf03a09491@185.209.223.44:26656,6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,20501e4b4d6eea8c2211e8da79c499549e5bb629@185.196.20.33:27656,22fa766ffe457fd1236ea88bce1f40bf4bbaf328@77.91.100.131:26656,5a27e76e81cf59978ae271e0f7d53d8d15ecb282@89.163.209.173:40656,f916eaa4d614541f97df358788ddeb689e487b0b@149.202.73.104:10256,6b8021f2cf9bdad927473dd6cb075a83787a268a@89.179.33.100:26656,f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,a6a8aeea2cb22e2aa18698bfd676047d2a8275a6@173.212.251.224:30656,6225f30c704d879ef61161450ebe9dc14681916a@144.126.138.161:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
